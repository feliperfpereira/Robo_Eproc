
import pytest

from src.scripts.relatorio_conclusos import RelatorioConclusos


@pytest.fixture
def relatorio_scraper():
    return RelatorioConclusos()

@pytest.mark.asyncio
async def test_relatorio_conclusos_initialization(relatorio_scraper):
    assert relatorio_scraper is not None

@pytest.mark.asyncio
async def test_relatorio_run_method_exists(relatorio_scraper):
    assert hasattr(relatorio_scraper, 'run')
    assert callable(relatorio_scraper.run)
