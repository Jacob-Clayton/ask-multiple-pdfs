css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #475063
}
.chat-message.bot {
    background-color: #555f77
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 60px;
  max-height: 60px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 95%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.svgrepo.com/show/306500/openai.svg" style="max-height: 60px; max-width: 60px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.svgrepo.com/show/307893/internet-user-software-engineer-programmer-software-developer.svg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
