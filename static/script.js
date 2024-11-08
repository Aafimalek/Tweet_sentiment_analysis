async function analyze() {
    const username = document.getElementById("username").value;
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "<p>Analyzing tweets...</p>";

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username })
        });
        const data = await response.json();

        if (data.error) {
            resultsDiv.innerHTML = `<p class="error">Error: ${data.error}</p>`;
        } else {
            resultsDiv.innerHTML = "<h3>Results:</h3>";
            data.tweets.forEach((tweet, i) => {
                const sentimentClass = data.sentiments[i] === 1 ? "sentiment-positive" : "sentiment-negative";
                const sentiment = data.sentiments[i] === 1 ? "Positive" : "Negative";
                resultsDiv.innerHTML += `<div class="tweet">${tweet} - <span class="${sentimentClass}">${sentiment}</span></div>`;
            });
        }
    } catch (error) {
        resultsDiv.innerHTML = "<p>Error fetching data.</p>";
    }
}
