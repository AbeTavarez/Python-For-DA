
#? Absolute Path
# C:\Users\Abraham\Desktop\da\python_mod\text_file_processing\my_file.txt

#? Relative Path
# text_file_processing\my_file.txt

# Open the file
file = open('./data/my_file.txt', encoding='cp1252')

# try:
#     print(file.name)
#     print(file.mode)
#     print(file.encoding)
#     print(file.read())
# finally:
#     # Close the file
#     file.close()

# =============

with open('./data/my_file.txt', encoding='cp1252', mode='r+') as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    # print(file.read(100))
    # print(file.read())
    
    # One line at a time
    # print(file.readline())
    
    # Returns a list of lines
    # print(file.readlines())
    lines = file.readlines()
    print(lines[-1])
    
    
# Using the same file created from previous section
with open('./data/my_file.txt', mode = 'r+') as fo:
  print(fo.read(3)) # prints 'How'
  print(fo.tell())  # prints '3'
  fo.seek(45)    # moves the cursor from 3 to 45
  print(fo.tell()) # prints '45'
  # print(fo.read()) # prints 
  
  
# ==============================
# def write_names_to_file(names, file_path):
#     try:
#         with open(file_path, 'w') as fp:
#             for item in names:
#                 # fp.write("%s\n" % item)
#                 fp.write(f"{item}\n")
#                 print(item)
#             print('Names have been written to the file.')
#     except Exception as error:
#         print(f"An error occurred: {str(error)}")
        
def write_names_to_file(names, file_path):
    try:
        with open(file_path, 'w') as fp:
            fp.write('\n'.join(names))
        print('Names have been written to the file.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
        

# Example of using the function
names = ['Jessa', 'Eric', 'Bob']

#file_path = r'E:/files_Path/sales.txt'
file_path = r'sales.txt'

write_names_to_file(names, file_path)


names_list = ["\nHaseeb", "\nJames", "\nFig", "\nTano"]

with open(r'sales.txt', 'a+') as fp:
  fp.writelines(names_list)
  
  
  
with open('my_file_new.txt', mode = 'w', encoding = 'utf-8') as f:
  f.write('The first line\n')
  f.write('And this is the second line\n')
  f.write('This is currently the last line\n')

