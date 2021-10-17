test:
	poetry run python -m coverage run || exit $?
	poetry run python -m coverage report
	poetry run python -m coverage html -i
	echo 'DONE';

test-debug:
	poetry run python -m pytest -s -rf -vv -x tests

publish:
	poetry publish --build