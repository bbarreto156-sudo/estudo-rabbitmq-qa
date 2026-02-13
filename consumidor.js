const amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) throw error0;
    
    connection.createChannel((error1, channel) => {
        if (error1) throw error1;

        const queue = 'order_notifications';
        channel.assertQueue(queue, { durable: false });

        console.log(" [*] Aguardando mensagens em %s.", queue);

        channel.consume(queue, (msg) => {
            const order = JSON.parse(msg.content.toString());
            
            // Simulação de lógica de negócio
            console.log(" [v] Processando notificação para o pedido:", order.order_id);
            console.log(" [v] E-mail enviado para:", order.customer_email);
            
        }, { noAck: true });
    });
});