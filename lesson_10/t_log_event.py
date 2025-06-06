import pytest
from lesson_10.log_event import log_event, logs_reeder


class TestLogsPositive:

    def test_status_success_positive(self):
        username = "Ruslan"
        status = "success"
        level = "INFO"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"

    def test_status_expired_positive(self):
        username = "Ruslan"
        status = "expired"
        level = "WARNING"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"

    def test_status_failed_positive(self):
        username = "Ruslan"
        status = "failed"
        level = "ERROR"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"


class TestLogsNegative:

    def test_status_success_negative(self):
        username = "Ruslan"
        status = "success"
        level = "INFO"
        log_event(username, status)
        last_line = logs_reeder()

        status = "failed"
        level = "WARNING"
        username = "Alex"

        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"

    def test_status_expired_negative(self):
        username = "Ruslan"
        status = "expired"
        level = "WARNING"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"
        level = "ERROR"
        username = "Alex"

        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"

    def test_status_failed_negative(self):
        username = "Ruslan"
        status = "failed"
        level = "ERROR"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"
        level = "INFO"
        username = "Alex"

        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"