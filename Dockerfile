# ==========================================
# STAGE 1: The Builder
# ==========================================
# Use "AS" (uppercase) to name the stage
FROM python:3.12.3-slim AS builder

WORKDIR /app

# 1. Create a virtual environment to isolate dependencies
RUN python -m venv /opt/venv

# 2. Activate the virtual environment for the build stage
ENV PATH="/opt/venv/bin:$PATH"

# 3. Install dependencies
COPY requirements.txt .
# We use --no-cache-dir to keep the builder layer smaller, though it matters less here since this stage is discarded
RUN pip install --no-cache-dir -r requirements.txt


# ==========================================
# STAGE 2: The Runner (Final Image)
# ==========================================
FROM python:3.12.3-slim

WORKDIR /app

# 1. Copy the Virtual Environment from the Builder stage
#    This is the "Magic Step" that makes the image small.
COPY --from=builder /opt/venv /opt/venv

# 2. Activate the virtual environment in the final image
ENV PATH="/opt/venv/bin:$PATH"

# 3. Copy only the application code (Using .dockerignore is recommended here)
COPY . .

EXPOSE 8000

# 4. Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]