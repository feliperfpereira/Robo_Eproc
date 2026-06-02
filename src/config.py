
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    EPROC_LOGIN: str
    EPROC_SENHA: str
    EPROC_URL: str = 'https://eproc1.tjto.jus.br/eprocV2_prod_1grau/'
    EPROC_2FA_SECRET: str | None = None
    EPROC_PERFIL: str | None = None # Perfil de usuário (ex: DIRETOR DE SECRETARIA)

    # Configurações do Navegador
    HEADLESS: bool = True
    BROWSER_CHANNEL: str = 'chrome' # chrome, msedge, chromium
    LOG_LEVEL: str = 'INFO'

    # Integração LegalMind Core
    LEGALMIND_API_URL: str = 'http://localhost:8000/api/v1/'
    LEGALMIND_API_KEY: str | None = None

    # Autenticação do Robô (necessário para o modo API)
    API_KEY: str | None = None

    # Integração Google Drive e Google Sheets
    GOOGLE_APPLICATION_CREDENTIALS: str | None = None
    GOOGLE_DRIVE_FOLDER_ID: str | None = None
    GOOGLE_SHEETS_SPREADSHEET_ID: str = '1ZoB5WItw1KwY4zIkrfLhAtWmgIDMbLNJRaCSM0Il6po'

    # Relatório de Processos Conclusos e N8N
    RELATORIO_CONCLUSOS_PATH: str = r'G:\Meu Drive\Processos_Conclusos.csv'
    N8N_WEBHOOK_PLANILHA: str = 'https://n8n.maicondener.dev.br/webhook/planilha-processos-gabinete'
    TEMP_DOWNLOAD_DIR: str = 'data'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

settings = Settings()
