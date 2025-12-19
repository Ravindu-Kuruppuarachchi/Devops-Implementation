# ==========================================
# STAGE 1: The Builder
# ==========================================
FROM python:3.12.3-slim as builder

WORKDIR /app

# 1. Create a virtual environment to isolate dependencies
RUN python -m venv /opt/venv

# 2. Activate the virtual environment for the build stage
#    (Any command run after this uses the venv python/pip)
ENV PATH="/opt/venv/bin:$PATH"

# 3. Install dependencies into the virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# ==========================================
# STAGE 2: The Runner (Final Image)
# ==========================================
FROM python:3.12.3-slim

WORKDIR /app

# 1. Copy the Virtual Environment from the Builder stage
#    (We copy the whole folder /opt/venv)
COPY --from=builder /opt/venv /opt/venv

# 2. Activate the virtual environment in the final image
#    (So that 'uvicorn' is found in the path)
ENV PATH="/opt/venv/bin:$PATH"

# 3. Copy the application code
COPY . .

EXPOSE 8000

# 4. Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]