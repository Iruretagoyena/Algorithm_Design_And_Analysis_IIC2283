tests="27"

for number in `seq 0 $tests`; do
    padded=$(printf %02d $number)
    echo $'\n'
    echo "RUNNING TEST ${padded}"
    OUTPUT=$(cat tests/p2/input/input${padded}.txt | time python p2.py)
    echo "Result: $OUTPUT"
    echo "Expected: $(cat tests/p2/output/output${padded}.txt)"
    if [ "$(echo "$OUTPUT" | tr -d '[:space:]')" = "$(cat tests/p2/output/output${padded}.txt | tr -d '[:space:]')" ]; then
        echo "PASSED"
    else
        echo "FAILED"
    fi
done
