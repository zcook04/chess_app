backend.up:
	source env/bin/activate && cd ./backend && uvicorn main:app --reload

frontend.up:
	cd ./frontend && npm run dev

both.up:
	make backend.up& make frontend.up