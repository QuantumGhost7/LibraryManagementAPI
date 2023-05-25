from rest_framework.decorators import api_view
from rest_framework.response import Response
from LibraryApp.models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=404)

@api_view(['POST'])
#@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
@api_view(['PUT'])
def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Book.DoesNotExist:
        return Response(status=404)

@api_view(['DELETE'])
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response(status=204)
    except Book.DoesNotExist:
        return Response(status=404)
