# Portfolio API

Backend API for the Portfolio Platform, built using Python and FastAPI.

This repository contains the independently executable backend application for the Portfolio Platform. The platform is being developed incrementally to demonstrate software engineering, system design, automation, security, and cloud-native development practices.

## 1. Current Implementation

The API currently includes:

- A minimal FastAPI application.
- A root endpoint (`GET /`) returning `{"message": "Portfolio API"}`.
- Environment configuration and validation during application startup.
- Automated tests covering configuration, startup, and endpoint behavior.
- Reproducible Python dependency management using `uv` and a committed lockfile.

**Not implemented yet:** Authentication, database persistence, business APIs, background processing integration, containerization, or deployment.

These capabilities will be introduced through their respective Jira work items.

## 2. Prerequisites

The following tools are needed to set up and run the application.

| Tool | Required Version | Purpose |
|---|---|---|
| Git | Recent supported version | Clone and manage the repository |
| Python | 3.13 or newer | Application runtime |
| uv | Recent compatible version | Python installation, virtual environments, and dependency management |
| curl | Optional | Test HTTP endpoints |

Python can be installed and managed through `uv`, so a separate system-wide Python installation is not mandatory.

### 2.1 Installing prerequisites

**macOS**

If Homebrew is installed:

```bash
brew install git uv
```

Install Python 3.13 through uv:

```bash
uv python install 3.13
```

Homebrew installation instructions: https://brew.sh/

**Linux**

Install Git using your distribution's package manager.

Install uv using the official instructions:

https://docs.astral.sh/uv/getting-started/installation/

Then install Python:

```bash
uv python install 3.13
```

**Windows**

Install Git and uv using their official installation instructions.

Git: https://git-scm.com/install/

uv: https://docs.astral.sh/uv/getting-started/installation/

Then install Python:

```powershell
uv python install 3.13
```

### 2.2 Verify prerequisites

Confirm the required tools are accessible:

```bash
git --version
uv --version
uv python list --only-installed
```

The installed Python list should include a compatible Python 3.13+ interpreter.

**Platform validation:** The current setup has been tested on macOS. Linux and Windows installation guidance is provided for portability but has not yet been independently validated.

## 3. Clone and Install

Clone the repository:

```bash
git clone https://github.com/Abishek2905/portfolio-api.git
cd portfolio-api
```

Install the project dependencies:

```bash
uv sync --locked
```

This command:

- Uses the committed `uv.lock` dependency resolution.
- Creates the project virtual environment if necessary.
- Installs the application's required and development dependencies.
- Fails if the lockfile needs to be updated.

The project uses Python 3.13 or newer as specified in `pyproject.toml`.

`uv` manages the virtual environment automatically. Manual virtual-environment creation or activation is not required for the commands in this README.

## 4. Environment Configuration

The API uses the `PORTFOLIO_ENV` environment variable to identify its runtime environment.

| Value | Description |
|---|---|
| `development` | Local development |
| `test` | Automated testing |
| `production` | Production environment identifier |

### Default behavior

If `PORTFOLIO_ENV` is not defined, the application defaults to `development`.

The application also:

- Removes leading and trailing whitespace.
- Converts values to lowercase.
- Rejects unsupported or explicitly empty values with `ValueError`.

For example, `PORTFOLIO_ENV=" PRODUCTION "` is normalized to `production`.

### Setting the environment

On macOS or Linux:

```bash
PORTFOLIO_ENV=test uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

On Windows PowerShell:

```powershell
$env:PORTFOLIO_ENV = "test"
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Environment example file

The repository contains `.env.example`, documenting the supported configuration values.

**Important:** The application reads variables from the process environment using `os.getenv()`.

It does not automatically load `.env` or `.env.example`. Creating or copying either file alone will not change the environment used by the application.

Local environment files and credentials must not be committed to Git.

Selecting `PORTFOLIO_ENV=production` does not automatically provision production infrastructure or make the application production-ready.

## 5. Run the Application

Start the API locally:

```bash
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

For local development with automatic code reload:

```bash
uv run uvicorn app.main:app --reload
```

The application should start successfully and report the selected environment.

Open the root endpoint:

http://127.0.0.1:8000/

Expected JSON response:

```json
{
  "message": "Portfolio API"
}
```

Alternatively, from another terminal:

```bash
curl -i http://127.0.0.1:8000/
```

Expected HTTP status: `200 OK`.

Stop the application using `Ctrl+C`.

### Startup validation

Configuration validation occurs during the FastAPI application lifespan startup.

If `PORTFOLIO_ENV` contains an unsupported value, application startup fails rather than proceeding with an invalid configuration.

## 6. Run Automated Tests

Run all tests:

```bash
uv run pytest -v
```

The existing test suite covers:

- Default environment configuration.
- Normalization of supported values.
- Rejection of invalid and empty environment values.
- Root endpoint behavior.
- Successful startup with valid configuration.
- Startup failure with invalid configuration.

**Latest verified result (macOS, 23 October 2026):** 10 tests passed.

One non-blocking `StarletteDeprecationWarning` was observed from the installed FastAPI/Starlette testing dependencies. Dependency-maintenance changes are tracked separately.

## 7. Troubleshooting

### `git`, `uv`, or Python is not found

Verify that the required tools are installed and available in your terminal's PATH.

Use the official installation instructions in Section 2.

### Dependency synchronization fails

Verify:

- The current directory is the repository root.
- `pyproject.toml` and `uv.lock` are present.
- A compatible Python version is available.
- The reported dependency resolution or installation error.

Do not regenerate the lockfile unnecessarily to resolve an unrelated local setup issue.

### Port 8000 is already in use

Stop the existing application or use another port:

```bash
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### Invalid `PORTFOLIO_ENV`

If application startup fails with `Invalid PORTFOLIO_ENV`, verify that the variable contains one of:

- `development`
- `test`
- `production`

The value must not be empty.

### Changes to `.env` have no effect

The application does not currently load `.env` automatically.

Set `PORTFOLIO_ENV` in the process environment as described in Section 4.

### Tests report a dependency warning

A warning is not necessarily a test failure. Review the warning separately from the pytest pass/fail result.

## 8. Repository Responsibilities

The Portfolio Platform separates application responsibilities across repositories.

| Repository | Responsibility |
|---|---|
| `portfolio-api` | Backend HTTP APIs and application logic |
| `portfolio-web` | Frontend application |
| `portfolio-worker` | Background-processing component |
| `portfolio-platform` | Cross-repository local orchestration and integration setup |

The orchestration repository does not own shared application or domain logic.

## 9. Development and Roadmap

Development follows an incremental, requirement-driven approach.

Future work includes database integration, authentication, business APIs, containerization, automated CI/security checks, and deployment.

Technical decisions, implementation scope, testing evidence, and delivery progress are tracked through Jira, GitHub pull requests, and the Portfolio Platform's Confluence documentation.

This README documents only the currently supported application setup and behavior.
