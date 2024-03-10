import os
import zipfile


class ZsDic:
    def __init__(self):

        self.zip_controller = zipfile.ZipFile(
            os.path.join(
                os.path.dirname(
                    os.path.abspath(
                        __file__
                    )
                ), "ZsDic.zip"
            ), mode='r'
        )

    def get_dict(self, dict_type: str):
        """
        :param dict_type: type of dictionary to return. Can be 'zs', 'pack', 'bcett', or 'byml'
        :return: bytes or binary data
        """

        match dict_type:

            case 'zs':
                return self.zip_controller.read(name='zs.zsdic')

            case 'pack':
                return self.zip_controller.read(name='pack.zsdic')

            case 'bcett':
                return self.zip_controller.read(name='bcett.byml.zsdic')

            case 'byml':
                return self.zip_controller.read(name='bcett.byml.zsdic')

        raise ValueError(
            "dict_type param may either be 'zs', 'pack', 'bcett', or 'byml'. It can't be " + dict_type
        )
