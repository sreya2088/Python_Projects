#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_phone():
    while True:
        want_phone = input('Do you want a phone? (Yes or No): ')

        if want_phone.lower() == 'no':
            print('Thank you! Have a great day.')
            break
        elif want_phone.lower() == 'yes':
            phone_preference = input('Which phone do you want? (iPhone or Samsung): ')

            if phone_preference.lower() == 'iphone':
                while True:
                    iphone_model = input('Which iPhone model do you want? (13, 14, or 15): ')

                    if iphone_model.lower() in ['13', '14', '15']:
                        break
                    else:
                        print('Invalid choice for iPhone model. Please specify 13, 14, or 15.')

                while True:
                    storage_variant = input('Which storage variant do you prefer? (128, 256, or 512): ')

                    if storage_variant in ['128', '256', '512']:
                        break
                    else:
                        print('Invalid choice for storage variant. Please specify 128, 256, or 512.')

                while True:
                    color_preference = input('Which color do you want? (White, Red, Black): ')

                    if color_preference.lower() in ['red', 'white', 'black']:
                        break
                    else:
                        print('Invalid choice for color. Please specify White, Red, or Black.')

                print(f'Great choice! You want the iPhone {iphone_model} with {storage_variant}GB storage in {color_preference.lower()}.')

                print('Here are the specifications:')
                print('Price: Rs 40000/-')
                print('Camera: 12MP + 12MP')
                print('Battery: Up to 20 hours of video playback')
                print('Accessories: Earbuds, USB-C Power Adapter')
                

            elif phone_preference.lower() == 'samsung':
                while True:
                    samsung_model = input('Which Samsung model do you want? ("samsung galaxy s21" or "samsung galaxy s22"): ')

                    if samsung_model.lower() in ['samsung galaxy s21', 'samsung galaxy s22']:
                        break
                    else:
                        print('Invalid choice for Samsung model. Please specify "samsung galaxy s21" or "samsung galaxy s22".')

                while True:
                    storage_variant = input('Which storage variant do you prefer? (128, 256, or 512): ')

                    if storage_variant in ['128', '256', '512']:
                        break
                    else:
                        print('Invalid choice for storage variant. Please specify 128, 256, or 512.')

                while True:
                    color_preference = input('Which color do you want? (White, Red, Black): ')

                    if color_preference.lower() in ['red', 'white', 'black']:
                        break
                    else:
                        print('Invalid choice for color. Please specify White, Red, or Black.')

                print(f'Great choice! You want the Samsung {samsung_model} with {storage_variant}GB storage in {color_preference.lower()}.')

                print('Here are the specifications:')
                print('Price: Rs 20000/-')
                print('Camera: 10MP + 12MP')
                print('Battery: Up to 15 hours of video playback')
                print('Accessories: Earbuds, USB-C Power Adapter')

            else:
                print('Invalid choice for phone preference. Please specify iPhone or Samsung.')
        else:
            print('Invalid choice. Please specify Yes or No.')

def main():
    get_phone()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




