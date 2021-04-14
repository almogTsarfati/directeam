from flask import Flask, render_template, request, jsonify
import boto3

client = boto3.client('sqs')
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    content = request.json
    print(content)
    response = client.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/430771376827/data_pipeline',
    MessageBody = str(content)
    # MessageAttributes= 'test messege'
    )
    return response



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')