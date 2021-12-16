tests="6"

for number in `seq 0 $tests`; do
    padded=$(printf %02d $number)
    echo $'\n'
    echo "RUNNING TEST ${padded}"
    OUTPUT=$(cat tests/p1/input/input${padded}.txt | time python p1.py)
    echo "Result: $OUTPUT"
    VALID=$(python tests/p1/is_prime.py $(cat tests/p1/input/input${padded}.txt) $OUTPUT)
    if [ "$VALID" = "1" ]; then
        echo "PASSED"
    elif  [ "$VALID" = "-1" ]; then
        echo "NO PRIMES, CHECK MANUALLY"
    else
        echo "FAILED"
    fi
done
