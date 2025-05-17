from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import SignupSerializer, LoginSerializer
from .models import User
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



def get_access_token_for_user(user):
    token = AccessToken.for_user(user)
    return str(token)


class RoleSignupView(APIView):
    role = None  # 'patient', 'doctor', 'pharmacist'

    def post(self, request):
        serializer = SignupSerializer(
            data=request.data, context={'role': self.role})
        if serializer.is_valid():
            user = serializer.save()
            token = get_access_token_for_user(user)

            return Response({
                'user': {
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'is_patient': user.is_patient,
                    'is_doctor': user.is_doctor,
                    'is_pharmacist': user.is_pharmacist,
                },
                'access': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleLoginView(APIView):
    role_flag_map = {
        'patients': 'is_patient',
        'doctors': 'is_doctor',
        'pharmacies': 'is_pharmacist',
    }

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # 'patients', 'doctors', etc.
            path_segment = request.path.strip('/').split('/')[0]
            expected_flag = self.role_flag_map.get(path_segment)

            if expected_flag and not getattr(user, expected_flag, False):
                return Response({'detail': 'Unauthorized for this role.'}, status=status.HTTP_403_FORBIDDEN)

            token = get_access_token_for_user(user)
            return Response({'access': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Refresh token required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({'detail': 'Invalid or expired refresh token.'}, status=status.HTTP_400_BAD_REQUEST)

            
# Views per role
class PatientSignupView(RoleSignupView):
    role = 'patient'


class DoctorSignupView(RoleSignupView):
    role = 'doctor'


class PharmacySignupView(RoleSignupView):
    role = 'pharmacist'


class PatientLoginView(RoleLoginView):
    pass


class DoctorLoginView(RoleLoginView):
    pass


class PharmacyLoginView(RoleLoginView):
    pass
