#Creator by KEHAN
from PIL import Image, ImageFilter
from colorama import Fore

'''Структура роботи програми'''
def blur_image(image_path): # Розмиття зображення
  with Image.open(image_path) as img: # Робота з картникою
    blur_img = img.filter(ImageFilter.BLUR)
    blur_img.show()
    return blur_img
  
def coup_image(image_path): # Повернути зображення на 180*
  with Image.open(image_path) as img: # Робота з картникою
    converted_img = img.transpose(Image.ROTATE_180)
    converted_img.show()
    return coup_image
  bw_img.show()

def convert_to_bw(image_path): # Чорнобіле зображення
  with Image.open(image_path) as img: # Робота з картникою
    bw_img = img.convert('L')
    bw_img.show()
    return convert_to_bw
  
if __name__ == '__main__':
  image_path = 'original.jpg'
  """Код USER"""
  while True:
    image_path = input(Fore.RED + "Введіть шлях до зображення (наприклад, 'original.jpg'): ")
    print(Fore.GREEN + "\nЩо ви хочете зробити з зображенням?")
    print("1. Перетворити на чорно-біле")
    print("2. Розмити зображення")
    print("3. Повернути зображення на 180 градусів")
    print('4. Зробити все')

    choice = input("Введіть номер операції (1, 2, 3 або 4): ")

    if choice == '1':
        convert_to_bw(image_path)

    elif choice == '2':
        blur_image(image_path)

    elif choice == '3':
        coup_image(image_path)

    elif choice == '4':
      convert_to_bw(image_path)
      blur_image(image_path)
      coup_image(image_path)
        
      
    else:
        print("Неправильний вибір! Спробуйте знову")
        
    replase = input('Повторити? (Напиши go, якщо ні то просто натисніть ENTER)): ')

    if replase.lower() != 'go':
      break

    else:
       pass
      