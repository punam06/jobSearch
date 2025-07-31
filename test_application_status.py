#!/usr/bin/env python
"""
Test script to verify the Application Status Update Feature
Run this after setting up some test data
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from jobs.models import Job, Application

def test_application_status_feature():
    """Test the application status functionality"""
    print("🚀 Testing Application Status Update Feature")
    print("=" * 50)
    
    # Test 1: Check if status field exists and has correct choices
    print("✅ Test 1: Checking Application model status field...")
    app = Application.objects.first()
    if app:
        print(f"   📄 Sample application status: {app.status} ({app.get_status_display()})")
        print(f"   🎨 Status color class: {app.get_status_color()}")
        print(f"   📅 Applied: {app.applied_at}, Updated: {app.updated_at}")
    else:
        print("   ⚠️  No applications found. Create some test data first.")
    
    # Test 2: Check status choices
    print("\n✅ Test 2: Available status choices...")
    for value, label in Application.STATUS_CHOICES:
        print(f"   • {value}: {label}")
    
    # Test 3: Check filtering functionality
    print("\n✅ Test 3: Testing status filtering...")
    for status_value, status_label in Application.STATUS_CHOICES:
        count = Application.objects.filter(status=status_value).count()
        print(f"   📊 {status_label}: {count} applications")
    
    # Test 4: Check data consistency
    print("\n✅ Test 4: Data consistency check...")
    total_apps = Application.objects.count()
    pending_apps = Application.objects.filter(status='pending').count()
    approved_apps = Application.objects.filter(status='approved').count()
    rejected_apps = Application.objects.filter(status='rejected').count()
    
    print(f"   📈 Total applications: {total_apps}")
    print(f"   ⏳ Pending: {pending_apps}")
    print(f"   ✅ Approved: {approved_apps}")
    print(f"   ❌ Rejected: {rejected_apps}")
    print(f"   🔍 Sum check: {pending_apps + approved_apps + rejected_apps} = {total_apps}")
    
    if pending_apps + approved_apps + rejected_apps == total_apps:
        print("   ✅ Data consistency: PASSED")
    else:
        print("   ❌ Data consistency: FAILED")
    
    print("\n🎉 Application Status Feature Test Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_application_status_feature()
