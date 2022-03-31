
class FileManagement(object):

    def __init__(self) -> None:
        pass

    def write(text:str, file:str):
        text_file = open(f'{file}.txt','w')
        text_file.write(text)
        text_file.close()