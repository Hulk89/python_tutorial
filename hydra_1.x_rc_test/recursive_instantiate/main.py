import hydra
from omegaconf import DictConfig

def instantiate(conf):
    if hasattr(conf, "params"):
        dict_ = {}
        for key, sub_conf in conf.params.items():
            if isinstance(sub_conf, DictConfig):
                if 'cls' in sub_conf:
                    dict_[key] = instantiate(sub_conf)
    return hydra.utils.instantiate(conf, **dict_)


@hydra.main(config_path='conf', config_name='config')
def my_app(cfg : DictConfig) -> None:
    print(cfg.pretty())
    obj = instantiate(cfg.parent_module)
    obj.print()
    print(obj.layer)

if __name__ == "__main__":
    my_app()
