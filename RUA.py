import sys

try:
    import app
except ImportError:
    sys.exit()

if __name__ == "__main__":
    app.approval()
    try:
        import LL
    except ImportError:
        sys.exit()
