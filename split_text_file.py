import os

def split_text_file(input_file, output_dir='arquivos_gerados', max_words=400000):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    words = content.split()
    total_words = len(words)
    print(f'Total words in file: {total_words}')

    file_count = 1
    start_idx = 0

    while start_idx < total_words:
        end_idx = start_idx + max_words
        output_file = os.path.join(output_dir, f"output_{file_count:03}.txt")

        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(' '.join(words[start_idx:end_idx]))
        
        print(f'{output_file} created with words from {start_idx} to {end_idx}')
        start_idx = end_idx
        file_count += 1

if __name__ == "__main__":
    try:
        split_text_file('arquivos_gerados/output.txt')
    except:
        print('Arquivo não encontrado.')