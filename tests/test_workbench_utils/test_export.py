import shutil

from anyio import Path

from workbench_utils.export import load_pipeline, remove_old_pipelines, save_pipeline


class FakePipeline:
    pass


def test_save_pipeline(tmp_path: Path):

    try:
        filepath = tmp_path / "fake_pipeline.pkl"
        save_pipeline(FakePipeline(), filepath)

        assert filepath.exists()

    finally:
        filepath.unlink()


def test_load_pipeline(tmp_path: Path):

    try:
        filepath = tmp_path / "fake_pipeline.pkl"
        save_pipeline(FakePipeline(), filepath)

        pipeline = load_pipeline(filepath)

        assert pipeline is not None

    finally:
        filepath.unlink()


def test_remove_old_pipelines(tmp_path: Path):

    try:
        dir_pipelines = tmp_path / "pipelines"
        dir_pipelines.mkdir(exist_ok=True, parents=True)

        save_pipeline(FakePipeline(), dir_pipelines / "fake_pipeline_01.pkl")
        save_pipeline(FakePipeline(), dir_pipelines / "fake_pipeline_02.pkl")

        remove_old_pipelines(dir_pipelines)

        assert not (dir_pipelines / "fake_pipeline_01.pkl").exists()
        assert not (dir_pipelines / "fake_pipeline_02.pkl").exists()

    finally:
        shutil.rmtree(dir_pipelines)
