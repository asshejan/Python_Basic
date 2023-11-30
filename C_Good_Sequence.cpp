#include <iostream>
#include <unordered_map>

using namespace std;

int min_removals_for_good_sequence(int N, int sequence[]) {
    unordered_map<int, int> count_dict;
    int removals = 0;

    // Count occurrences of each element in the sequence
    for (int i = 0; i < N; ++i) {
        count_dict[sequence[i]]++;
    }

    // Check for each element in the sequence
    for (int i = 0; i < N; ++i) {
        if (count_dict[sequence[i]] > sequence[i]) {
            removals += count_dict[sequence[i]] - sequence[i];
        }
    }

    return removals;
}

int main() {
    // Read input
    int N;
    cin >> N;

    int sequence[N];
    for (int i = 0; i < N; ++i) {
        cin >> sequence[i];
    }

    // Calculate and print the result
    int result = min_removals_for_good_sequence(N, sequence);
    cout << result << endl;

    return 0;
}
