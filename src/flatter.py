from typing import Iterable, Dict


class Flatter:

    @classmethod
    def flat_list(cls, data_list: Iterable):
        r = []
        for d in data_list:
            if isinstance(d, Iterable):
                r.extend(cls.flat_list(d))
            else:
                r.append(d)
        return r

    @classmethod
    def flat_dict(cls, data_dict: Dict, _key_prefix: str = None):
        r = {}
        for k, data in data_dict.items():

            if _key_prefix is None:
                kp = k
            else:
                kp = f'{_key_prefix}_{k}'

            if isinstance(data, Dict):
                r.update(cls.flat_dict(data, kp))
            elif isinstance(data, Iterable) and (not isinstance(data, str)):
                r.update(cls.__flat_dict_list(data, kp))
            else:
                r[kp] = data
        return r

    @classmethod
    def __flat_dict_list(cls, _data_list: Iterable, _key_prefix: str):
        _r = {}
        for _i, _d in enumerate(_data_list):
            if isinstance(_d, Dict):
                _r.update(cls.flat_dict(_d, f'{_key_prefix}_{_i}'))
            elif isinstance(_d, Iterable) and (not isinstance(_d, str)):
                _r.update(cls.__flat_dict_list(_d, f'{_key_prefix}_{_i}'))
            else:
                _r[f'{_key_prefix}_{_i}'] = _d
        return _r
