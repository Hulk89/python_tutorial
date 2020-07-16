import hydra
from omegaconf import DictConfig

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(cfg.pretty())
    print(cfg.db.passwd)

if __name__ == "__main__":
    my_app()
