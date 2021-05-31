from dataset.models.dataset import Dataset
from dataset.models.service import Service

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modellin(self, train, text) -> object:
        service = self.service
        pass

    def preprocess(self, train):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        print(f'train 의 type 은 {type(this.train)} 이다.')
        print(f'train 의 column 은 {(this.train.columns)} 이다.')
        print(f'train 의 type 은 {(this.train.head())} 이다.')
        print(f'train 의 type 은 {(this.train.tail())} 이다.')
