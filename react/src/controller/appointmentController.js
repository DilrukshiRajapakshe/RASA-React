import React, { Component } from 'react'
import { rasaAPI } from "../service/appointmentService"
import SMS_Cart from '../view/component/chatCard';

export const botAnswer = async(value) => {

    const name = "Dilrukshi";
    const dialogu = "මට දියවැඩියාව සම්බන්ධයෙන් වෛද්‍යවරයෙකු හමුවිය යුතුය";
    const data = await rasaAPI(name, dialogu);

    const question = value;
    const username = data.recipient_id;
    const answer = data.text;
    var showMessage =  false;

    if(question != null || username != null || answer != null){
        showMessage = true;
    }
    var user = {
        question : question,
        username : username,
        answer : answer,
        showMessage : showMessage
    }
    return user
}
