import os
import shutil
import hydra
from omegaconf import DictConfig

@hydra.main(config_path='conf', config_name='config')
def my_app(cfg : DictConfig) -> None:
    print(cfg.pretty())
    print("Working directory : {}".format(os.getcwd()))
    print(hydra.utils.get_original_cwd())
    print(hydra.utils.to_absolute_path(cfg.assets))
    # 현재 directory에서 working directory로 복사
    shutil.copytree(hydra.utils.to_absolute_path(cfg.assets), 
                    os.path.join(os.getcwd(), cfg.assets))

if __name__ == "__main__":
    my_app()
