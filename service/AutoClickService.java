package com.bulut.bulutautoclicker;

import android.accessibilityservice.AccessibilityService;
import android.accessibilityservice.GestureDescription;
import android.graphics.Path;
import android.view.accessibility.AccessibilityEvent;
import android.os.Handler;
import android.util.Log;

public class AutoClickService extends AccessibilityService {
    private static final String TAG = "BulutAutoClick";
    private static AutoClickService instance;
    
    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
        // Accessibility event handling
    }
    
    @Override
    public void onInterrupt() {
        Log.d(TAG, "Service interrupted");
    }
    
    @Override
    protected void onServiceConnected() {
        super.onServiceConnected();
        instance = this;
        Log.d(TAG, "Service connected");
    }
    
    @Override
    public void onDestroy() {
        instance = null;
        super.onDestroy();
    }
    
    public static AutoClickService getInstance() {
        return instance;
    }
    
    /**
     * Ekranda belirtilen koordinata tıklama yapar
     */
    public boolean performClick(float x, float y) {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
            Path clickPath = new Path();
            clickPath.moveTo(x, y);
            
            GestureDescription.Builder gestureBuilder = new GestureDescription.Builder();
            gestureBuilder.addStroke(new GestureDescription.StrokeDescription(clickPath, 0, 50));
            
            boolean result = dispatchGesture(gestureBuilder.build(), null, null);
            Log.d(TAG, "Click at (" + x + ", " + y + ") - Result: " + result);
            return result;
        }
        return false;
    }
    
    /**
     * Sürükleme hareketi yapar
     */
    public boolean performSwipe(float startX, float startY, float endX, float endY, long duration) {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
            Path swipePath = new Path();
            swipePath.moveTo(startX, startY);
            swipePath.lineTo(endX, endY);
            
            GestureDescription.Builder gestureBuilder = new GestureDescription.Builder();
            gestureBuilder.addStroke(new GestureDescription.StrokeDescription(swipePath, 0, duration));
            
            return dispatchGesture(gestureBuilder.build(), null, null);
        }
        return false;
    }
}
