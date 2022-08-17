from bibliotexparser import *
from dotenv import dotenv_values

def main():

    env = dotenv_values('.env')
    key = env['KEY']

    query_data = {'title':'', 'author':'', 'isbn':''}

    stop = False
    while not stop:
        print(f'''
        [1] Title = {query_data['title']}
        [2] Author = {query_data['author']}
        [3] ISBN = {query_data['isbn']}
        [4] Query
        ''')
        print('Input: ', end='')
        int_input = int(input())
        if int_input == 1:
            print('Title = ', end='')
            query_data['title'] = input()

        if int_input == 2:
            print('Author = ', end='')
            query_data['author'] = input()
        
        if int_input == 3:
            print('ISBN = ', end='')
            query_data['isbn'] = input()

        if int_input == 4:
            response = google_books_query(key=key,
                                          title  = query_data['title'],
                                          author = query_data['author'],
                                          isbn   = query_data['isbn'],
                                          tqdm=True)

            for i,volume in enumerate(response):
                author = ''
                title = ''

                try:
                    author = ', '.join(volume['authors'])
                except Exception: pass;

                try:
                    title = volume['title']
                except Exception: pass;

                print(f'[{i+1}] {author} - {title}')

            print(f'[X] Quit')
            print('Which book do I format?')
            print('Input: ', end='')
            int_input = int(input())

            if not (int_input in range(1, i+1, 1)): break;

            else:
                print()
                print(
                    google2bibtex(								# TODO: Ask for a entry name
                        volume=response[int_input-1],			# and for a entry type to 
                        entrytype='book', entryname='testname'	# properly format the text.
                        )
                    )

            stop = True

if __name__ == '__main__':
    main()
