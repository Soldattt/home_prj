from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_1(value_executed):
    assert (filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
        "EXECUTED") == value_executed)


def test_filter_by_state_2(value_canceled):
    assert (filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            "CANCELED") == value_canceled)


def test_filter_by_state_3(val_not):
    assert (filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]) == val_not)


def test_filter_by_state_4(value_random):
    assert (filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            "awdawd") == value_random)


def test_sort_reverse_true(sort_true):
    assert (sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]) == sort_true)

    assert (sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                          {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                          {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                          {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            True) == sort_true)


def test_sort_reverse_false(sort_false):
    assert (sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            False) == sort_false)


def test_date_len():
    assert (sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21"}]) == "Некорректный список")


def test_date(sort_date):
    assert (sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                         {"id": 939719570, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]) == sort_date)
