import hydra
from omegaconf import DictConfig, OmegaConf

def instantiate(conf, *args, **kwargs):
    if hasattr(conf, "params"):
        if 'args' in conf.params:
            args = list(args) + [instantiate(i) for i in conf.params.args]
            primitive_conf = OmegaConf.to_container(conf, resolve=True)
            del primitive_conf['params']['args']
            conf = DictConfig(primitive_conf)
    return hydra.utils.instantiate(conf, *args, **kwargs)


@hydra.main(config_path='conf', config_name='config')
def my_app(cfg : DictConfig) -> None:
    print(cfg.pretty())
    obj = instantiate(cfg.parent_module)
    print(obj)

if __name__ == "__main__":
    my_app()
