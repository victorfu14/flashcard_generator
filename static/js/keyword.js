function submitKeywords() {
    var values = $('input:checked').map(function() {
        return this.value;
    }).get();
    form = document.createElement('form');
    form.method = 'post';
    form.action = '/submit-keywords';
    hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'keywords';
    hiddenField.value = values;
    form.appendChild(hiddenField);
    hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'text';
    hiddenField.value = $('#text').text();
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
};