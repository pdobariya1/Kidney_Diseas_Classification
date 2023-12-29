from Kidney_Disease_Classification import logger
from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare base model"


class PrepareBaseModeTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModeTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========")
    except Exception as e:
        logger.exception(e)
        raise e