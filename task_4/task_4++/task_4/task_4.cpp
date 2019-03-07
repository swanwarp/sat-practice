//#include "pch.h"
#include <iostream>
#include <vector>
#include <string>
#include "testlib.h"
#include <sstream>

void check(std::vector<bool> R, int L, int K, std::vector<std::pair<int, int>> xy) {
	int N = R.size();

	for (int i = 0; i < N; i++) {
		if (!(-1 < xy[i].first < L and -1 < xy[i].second < L)) {
			quitf(_pe, "coordinates are supposed to be in range from 0 to L-1");
		}
	}

	for (int i = 0; i < N - 1; i++) {
		if (abs(xy[i].first - xy[i + 1].first) == abs(xy[i].second - xy[i + 1].second)) {
			quitf(_wa, "diagonal neighbours exists");
		}
	}

	int k = 0;

	for (int i = 0; i < N - 1; i++) {
		for (int j = i + 1; j < N; j++) {
			if (xy[i].first == xy[j].first and xy[i].second == xy[j].second) {
				quitf(_wa, "equal points exists");
			}

			if (R[i] and R[j] and (abs(xy[i].first - xy[j].first) == 1 or abs(xy[i].second - xy[j].second) == 1)) {
				k++;
			}
		}
	}

	if (k != K) {
		quitf(_wa, "energy is not equal to K %d %d", K, k);
	}
	else {
		quitf(_ok, "passed");
	}
}

std::pair<int, int> split(std::string s) {
	std::pair<int, int> result;
	std::istringstream ss(s);
	std::string token;

	std::getline(ss, token, ' ');
	result.first = std::stoi(token);
	std::getline(ss, token, ' ');
	result.second = std::stoi(token);

	return result;
}

int main(int argc, char* argv[]) {
	registerTestlibCmd(argc, argv);

	std::string p = inf.readLine();

	std::vector<bool> R;

	for (int i = 0; i < p.length(); i++) {
		R.push_back(p[i] == 'H');
	}

	int N = p.size();

	int L = inf.readInt();
	int K = inf.readInt();
	int x0 = inf.readInt();
	int y0 = inf.readInt();
	int x1 = inf.readInt();
	int y1 = inf.readInt();

	if (ans.readLine() == "unfolded") {
		if (ouf.readLine() == "unfolded") {
			quitf(_ok, "unfolded test ok");
		}
		else {
			quitf(_wa, "unfolded test isn't satisfied");
		}
	}
	else {
		std::vector<std::pair<int, int>> xy;

		while (!ouf.seekEof()) {
			xy.push_back(split(ouf.readLine()));
		}

		if (xy.size() != p.length()) {
			quitf(_pe, "missing points %d %d", p.length(), xy.size());
		}

		check(R, L, K, xy);
	}
}
