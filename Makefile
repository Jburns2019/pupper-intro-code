.DEFAULT_GOAL := john
john_file := Team-1/John_movement_commands.py
hendy_file := Team-1/Hendy_movement_commands.py
tim_file := Team-1/Tim_movement_commands.py
daniel_file := Team-1/Daniel_movement_commands.py

Rafael:
	git fetch upstream

#For John.
john:
	git add ${john_file}
	git commit -m "Simpler_update."
	git pull
	git push

run-john:
	git pull
	python ${john_file}

#For Hendy.
hendy:
	git add ${hendy_file}
	git commit -m "Simpler_update."
	git pull
	git push

run-hendy:
	git pull
	python ${hendy_file}

#For Tim.
tim:
	git add ${tim_file}
	git commit -m "Simpler_update."
	git pull
	git push

run-tim:
	git pull
	python ${tim_file}

#For Daniel.
daniel:
	git add ${daniel_file}
	git commit -m "Simpler_update."
	git pull
	git push

run-daniel:
	git pull
	python ${daniel_file}