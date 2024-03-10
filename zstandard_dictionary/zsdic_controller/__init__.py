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
                pass  # TODO: Stub

            case 'pack':
                pass  # TODO: Stub

            case 'bcett':
                pass  # TODO: Stub

            case 'byml':
                pass   # TODO: Stub

        raise ValueError(
            "dict_type param may either be 'zs', 'pack', 'bcett', or 'byml'. It can't be " + dict_type
        )
