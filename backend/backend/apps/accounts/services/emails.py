from common.services.email import BaseSendGridEmailTemplate

class SignUpAcceptedEmailTemplate(BaseSendGridEmailTemplate):
    template_id = 'd-d18d9a5efbae4f738099be5a72266f2c'
    required_template_variables = ['user_name', 'user_email']

    @staticmethod
    def prepare_email_content(instance):
        return {
            'user_name': instance.first_name,
            'user_email': instance.email
        }

    @staticmethod
    def get_email_subject(instance):
        return f'Hurray! Your New User Signup is created.'


class AdminVerifiedEmailTemplate(BaseSendGridEmailTemplate):
    template_id = 'd-4de71150b8bd4878a4cc480c84eccde7'
    required_template_variables = ['user_name', 'user_email']

    @staticmethod
    def prepare_email_content(instance):
        return {
            'user_name': instance.first_name,
            'user_email': instance.email
        }

    @staticmethod
    def get_email_subject(instance):
        return f'Hurray! Your User Account is verified.'