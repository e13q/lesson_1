# Requests to wttr.in

Executing requests with parameters on wttr.in to obtain information about the weather in Sheremetyevo, London, Cherepovets in black&white view with degrees Celsius, wind speed in m/s, only day&night mode and with “quiet” version enabled.

### How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Example of running script
```
$ python main.py
Sheremetyevo

      \   /     Ясно
       .-.      +9(7) °C
    ― (   ) ―   ↑ 3 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Сб. 25 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Clear          │
│      .-.      19 °C          │      .-.      15 °C          │
│   ― (   ) ―   ↗ 3-4 м/c      │   ― (   ) ―   ↗ 2-5 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Partly Cloudy  │     \   /     Clear          │
│  _ /"".-.     20 °C          │      .-.      +15(14) °C     │
│    \_(   ).   ↘ 4-5 м/c      │   ― (   ) ―   ↙ 2-5 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Пн. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │    \  /       Partly Cloudy  │
│      .-.      22 °C          │  _ /"".-.     17 °C          │
│   ― (   ) ―   ↖ 1 м/c        │    \_(   ).   ↑ 2-5 м/c      │
│      `-’      10 км          │    /(___(__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

London

     \  /       Переменная облачность
   _ /"".-.     16 °C
     \_(   ).   ↓ 1 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Пт. 24 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Overcast       │  _`/"".-.     Patchy rain ne…│
│      .--.     16 °C          │   ,\_(   ).   14 °C          │
│   .-(    ).   → 1-2 м/c      │    /(___(__)  ↙ 0-1 м/c      │
│  (___.__)__)  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│               0.0 мм | 0%    │     ‘ ‘ ‘ ‘   0.1 мм | 100%  │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Сб. 25 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Patchy rain ne…│               Cloudy         │
│   ,\_(   ).   19 °C          │      .--.     14 °C          │
│    /(___(__)  ↑ 2 м/c        │   .-(    ).   ↖ 1-2 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │  (___.__)__)  10 км          │
│     ‘ ‘ ‘ ‘   0.0 мм | 89%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой ливн…│    \  /       Partly Cloudy  │
│   ,\_(   ).   18 °C          │  _ /"".-.     +13(12) °C     │
│    /(___(__)  ↗ 5-7 м/c      │    \_(   ).   ↗ 3-5 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │    /(___(__)  10 км          │
│     ‘ ‘ ‘ ‘   0.3 мм | 100%  │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Cherepovec

      \   /     Clear
       .-.      +14(13) °C
    ― (   ) ―   ↗ 3 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤  Сб. 25 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │  _`/"".-.     Местами слабая │
│      .-.      24 °C          │   ,\_(   ).   16 °C          │
│   ― (   ) ―   ↗ 5-6 м/c      │    /(___(__)  ↘ 2-5 м/c      │
│      `-’      10 км          │      ‘ ‘ ‘ ‘  5 км           │
│     /   \     0.0 мм | 0%    │     ‘ ‘ ‘ ‘   0.4 мм | 100%  │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Вс. 26 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Солнечно       │
│      .-.      18 °C          │      .-.      +10(9) °C      │
│   ― (   ) ―   ↙ 3 м/c        │   ― (   ) ―   ↙ 1-3 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤  Пн. 27 мая ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │    \  /       Partly Cloudy  │
│      .-.      +23(24) °C     │  _ /"".-.     18 °C          │
│   ― (   ) ―   ↗ 2 м/c        │    \_(   ).   ↑ 2-4 м/c      │
│      `-’      10 км          │    /(___(__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
