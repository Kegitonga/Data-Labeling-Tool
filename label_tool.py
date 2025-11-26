"""label_tool.py - create TSV tasks for labeling and load results
"""
import csv

def create_tasks(items, path='tasks.tsv'):
    with open(path, 'w', newline='') as fh:
        writer = csv.writer(fh, delimiter='\\t')
        writer.writerow(['id','text'])
        for i,t in enumerate(items):
            writer.writerow([i,t])
    return path

if __name__ == '__main__':
    items = ['I love this product', 'Refund request: order 123']
    print('Tasks written to', create_tasks(items))
