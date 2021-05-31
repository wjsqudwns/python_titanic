from dataset.views.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = int(input('0:EXIT 1:Preprocess'))
        if menu == 0:
            break

        elif menu ==1:
            controller.preprocess('train.csv')

        else:
            continue