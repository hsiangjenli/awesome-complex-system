cleanup:
	cd docs && rm -rf build

build:
	make cleanup
	cd docs && make html