

from ..model.dbmodel import DesignerModel


def init():
    if not DesignerModel.exists():
        DesignerModel.create_table()


def main():
    print('db initializing started')
    init()
    print('db initializing done')


if __name__ == "__main__":
    init()
