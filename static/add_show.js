document.addEventListener('DOMContentLoaded', function() {
    // Get the number of shows
    const numShowsInput = document.getElementById('num_shows');

    numShowsInput.addEventListener('change', function() {
        const numShows = parseInt(numShowsInput.value);
        const showDetailsDiv = document.getElementById('show-details');
        showDetailsDiv.innerHTML = ''; 

        // Show details for the no. of shows
        for (let i = 0; i < numShows; i++) {
            const showDetailsFields = `
                <div class="show-details-fields">
                    <h3>Show ${i + 1}</h3>
                    <div class="form-group">
                        <label for="timing_${i}">Timing</label>
                        <input type="time" id="timing_${i}" name="timing_${i}" required>
                    </div>
                    <div class="form-group">
                        <label for="end_time_${i}">End Time</label>
                        <input type="time" id="end_time_${i}" name="end_time_${i}" required>
                    </div>
                    <div class="form-group">
                        <label for="no_of_balcony_seats_${i}">No. of Balcony Seats</label>
                        <input type="number" id="no_of_balcony_seats_${i}" name="no_of_balcony_seats_${i}" value="70" required>
                    </div>
                    <div class="form-group">
                        <label for="no_of_ordinary_seats_${i}">No. of Ordinary Seats</label>
                        <input type="number" id="no_of_ordinary_seats_${i}" name="no_of_ordinary_seats_${i}" value="190" required>
                    </div>
                    <div class="form-group">
                        <label for="balcony_rate_${i}">Balcony Rate</label>
                        <input type="number" id="balcony_rate_${i}" name="balcony_rate_${i}" value="180" required>
                    </div>
                    <div class="form-group">
                        <label for="ordinary_rate_${i}">Ordinary Rate</label>
                        <input type="number" id="ordinary_rate_${i}" name="ordinary_rate_${i}" value="120" required>
                    </div>
                </div>
            `;
            showDetailsDiv.insertAdjacentHTML('beforeend', showDetailsFields);
        }
    });
});
