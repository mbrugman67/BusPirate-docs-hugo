# merge first two (flash, bluetag)
python mergecast.py bluetag-sizzle.json i2c-sizzle.json sizzle-cast.json
# merge next (i2c)
python mergecast.py sizzle-cast.json sim-sizzle.json sizzle-cast.json
# sim
python mergecast.py sizzle-cast.json flash-sizzle.json sizzle-cast.json
# 1wire
python mergecast.py sizzle-cast.json 1wire-sizzle.json sizzle-cast.json
# sle4442
python mergecast.py sizzle-cast.json sle4442-sizzle.json sizzle-cast.json
pause