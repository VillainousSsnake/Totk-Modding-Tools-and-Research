import os
import zipfile


class ZsDic:
    @staticmethod
    def get_dict(dict_type: str) -> bytes:
        """
        :param dict_type: type of dictionary to return. Can be 'zs', 'pack', 'bcett', or 'byml'
        :return: bytes or binary data
        """

        zip_controller = zipfile.ZipFile(
            os.path.join(
                os.path.dirname(
                    os.path.abspath(
                        __file__
                    )
                ), "ZsDic.zip"
            ), mode='r'
        )

        match dict_type:

            case 'zs':
                return zip_controller.read(name='zs.zsdic')

            case 'pack':
                return zip_controller.read(name='pack.zsdic')

            case 'bcett':
                return zip_controller.read(name='bcett.byml.zsdic')

            case 'byml':
                return zip_controller.read(name='bcett.byml.zsdic')

        raise ValueError(
            "dict_type param may either be 'zs', 'pack', 'bcett', or 'byml'. It can't be " + dict_type
        )
