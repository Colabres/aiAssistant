from src.core.select import select_overrides

def test_select_exact():
    overrides = [{"q":"как тебя зовут", "a":"Меня зовут Алекса."}]
    picked = select_overrides("Как тебя зовут?", overrides, k=3)
    assert picked and picked[0]["a"] == "Меня зовут Алекса."

def test_select_fuzzy():
    overrides = [{"q":"откуда ты", "a":"Из страны сказок."}]
    picked = select_overrides("ты откуда вообще", overrides, k=3)
    assert picked and picked[0]["a"].startswith("Из страны")
