HEALTHY=False
for i in $(seq 1 15); do
    echo "Health check attempt: $i"

    if curl -fsS \
        --connect-timeout 2 \
        --max-time 5 \
        http://127.0.0.1:18081/ \
        -o /dev/null; then

        HEALTHY=true
        echo "SUCCESS: Target environment is healthy!"
        break
    fi

    echo "Connection failed. Retrying..."
    sleep 2
done

echo $HEALTHY