

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int margin_left = 0, margin_right = nums1Size;
    int tmp1_left, tmp2_left, tmp1_right, tmp2_right;
    if(nums1Size==0){
        if(nums2Size&1)
            return nums2[nums2Size/2];
        else
            return (nums2[nums2Size/2-1] + nums2[nums2Size/2])/2.0;
    }
    if(nums2Size==0){
        if(nums1Size&1)
            return nums1[nums1Size/2];
        else
            return (nums1[nums1Size/2-1] + nums1[nums1Size/2])/2.0;
    }
    while(margin_left <= margin_right){
        int x = margin_left + (margin_right - margin_left) / 2;
        int y = (nums1Size + nums2Size) / 2 - x;
        if(y > nums2Size){
            margin_left = x;
            continue;
        }
        if(y < 0){
            margin_right = x;
            continue;
        }
        if(x) tmp1_left = nums1[x-1]; else tmp1_left = NULL;
        if(x != nums1Size) tmp1_right = nums1[x]; else tmp1_right = NULL;
        if(y) tmp2_left = nums2[y-1]; else tmp2_left = NULL;
        if(y != nums2Size) tmp2_right = nums2[y]; else tmp2_right = NULL; 
        
        if(tmp1_left!=NULL && tmp2_right!=NULL)
            if(tmp1_left > tmp2_right){
                margin_right = x;
                continue;
            }
        if(tmp2_left!=NULL && tmp1_right!=NULL)
            if(tmp2_left > tmp1_right){
                margin_left = x+1;
                continue;
            }
        break;
    }
    
    if((nums1Size + nums2Size) & 1){
        return tmp1_right == NULL? tmp2_right : (tmp2_right == NULL? tmp1_right: (tmp1_right > tmp2_right ? tmp2_right: tmp1_right));
    }
    else{
        int left, right;
        left = tmp1_left == NULL? tmp2_left:(tmp2_left==NULL?tmp1_left:(tmp1_left>tmp2_left?tmp1_left:tmp2_left));
        right = tmp1_right == NULL? tmp2_right : (tmp2_right == NULL? tmp1_right: (tmp1_right > tmp2_right ? tmp2_right: tmp1_right));
        return (left + right) / 2.0;
    }
    
}
