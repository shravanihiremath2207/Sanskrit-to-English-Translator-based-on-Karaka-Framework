import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset

# Define the class to represent the dataset with labeled karakas
class KarakaDataset(Dataset):
    def __init__(self, sentences, karakas, tokenizer, max_length):
        self.sentences = sentences
        self.karakas = karakas
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, idx):
        sentence = self.sentences[idx]
        karakas = self.karakas[idx]
        inputs = self.tokenizer.encode_plus(
            sentence,
            add_special_tokens=True,
            padding='max_length',
            truncation=True,
            max_length=self.max_length,
            return_tensors='pt'
        )
        return {
            'input_ids': inputs['input_ids'].flatten(),
            'attention_mask': inputs['attention_mask'].flatten(),
            'karaka_labels': {
                'kartru': karakas['kartru'],
                'karma': karakas['karma'],
                'kriya': karakas['kriya'],
                'sampradan': karakas['sampradan'],
                'apadan': karakas['apadan'],
                'karan': karakas['karan']
            }
        }

def fine_tune_bert():
    # Load the dataset from the CSV file
    dataset_path = "karakas.csv"
    df = pd.read_csv(dataset_path)

    # Create an instance of the BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    # Prepare the data for fine-tuning
    sentences = df['sentence'].tolist()
    karakas = df['karakas'].tolist()
    max_length = 128  # Set the maximum sequence length for BERT
    dataset = KarakaDataset(sentences, karakas, tokenizer, max_length)
    data_loader = DataLoader(dataset, batch_size=8, shuffle=True)

    # Define the optimizer and loss function
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
    loss_fn = torch.nn.CrossEntropyLoss()

    # Fine-tuning loop
    model.train()
    for epoch in range(3):
        total_loss = 0
        for batch in data_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            karaka_labels = batch['karaka_labels']

            outputs = model(input_ids, attention_mask=attention_mask)
            loss = 0
            for karaka, label in karaka_labels.items():
                if label is not None:
                    label_id = tokenizer.encode(label, add_special_tokens=False)
                    label_id = torch.tensor(label_id).unsqueeze(0)
                    loss += loss_fn(outputs.logits[0], label_id)

            total_loss += loss.item()
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        print(f"Epoch {epoch+1}, Loss: {total_loss}")

    # Save the fine-tuned model
    model.save_pretrained('fine_tuned_bert')

if __name__ == "__main__":
    fine_tune_bert()
